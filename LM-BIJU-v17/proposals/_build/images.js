// LM BIJU · unified image pipeline (v3)
// Every source photo → sRGB, metadata stripped, AVIF + WebP (all sizes) + one JPEG fallback.
// Output: proposals/assets/img/{legacy,mj}, proposals/assets/video, proposals/assets/manifest.json
// Run: NODE_PATH=<dir with sharp> node proposals/_build/images.js
const sharp = require('sharp'), fs = require('fs'), path = require('path');
sharp.concurrency(2);
const ROOT = path.resolve(__dirname, '../..');                 // LM-BIJU-v17/
const IMG = ROOT + '/images', MJ = ROOT + '/_research/mj-uploads';
const OLDV = ROOT + '/_research/demo-b/assets/video';          // graded 48 frames + mobile loop from stage B
const OUT = ROOT + '/proposals/assets';
for (const d of ['img/legacy', 'img/mj', 'video']) fs.mkdirSync(OUT + '/' + d, { recursive: true });

const RATIO = { p: 4 / 5, v: null, l: 3 / 2, w: 21 / 9, s: 3 / 2, t: 4 / 5 };
// kind → widths; jpg = the single JPEG fallback width
const SIZES = { p: [480, 800, 1200], v: [600, 900, 1200], l: [600, 900], w: [960, 1680], s: [800, 1080], t: [480, 576] };
const JPG = { p: 800, v: 900, l: 900, w: 960, s: 800, t: 480 };

// ---------- legacy (all 17 files in images/) ----------
const LEG = {
  'hero-aco':       { kinds: { v: {}, p: {}, p2: { base: 'p', position: 'bottom' } } },
  'cat-homem':      { kinds: { v: {}, p: {} } },
  'hero-ouro':      { kinds: { p: {} } },
  'colar-topazio':  { kinds: { p: {} } },
  'argolas-pave':   { kinds: { p: {} } },
  'pulseira-rosa':  { kinds: { p: {}, p2: { base: 'p', position: 'top' } } },
  'cat-colares':    { kinds: { p: {} } },
  'brincos-safira': { kinds: { p: {} } },
  'hero-still':     { kinds: { p: {} } },
  'cat-relogios':   { kinds: { p: {} } },
  'cat-aneis':      { kinds: { p: {}, p2: { base: 'p', position: 'bottom' } } },
  'cat-pulseiras':  { kinds: { p: {} } },
  'cat-brincos':    { kinds: { p: {}, l: {} } },
  'cat-loja':       { kinds: { p: {}, p2: { base: 'p', position: 'right' }, l: {} } },
  'cat-moda':       { kinds: { p: {}, l: {} } },
  'anel-solitario': { kinds: { v: {}, p: {} } },
  'pendente-halo':  { kinds: { p: {} }, thirdParty: 'Caixa com a marca "Emiza Jewellery" (terceiros) — só como imagem editorial temporária' },
};
// ---------- MJ: 12 keepers + 7 acceptable (stage-a screening) ----------
const JOB = { g1: 'f8a529de', g2: '0ba8b142', g3: '019548e8', g4: '2df68861', g5: 'b0ae1130', g6: 'd2be353e', g7: '80a9bf07' };
const MJS = {
  'g3-2': 'ws', 'g4-0': 'w', 'g5-0': 'wt', 'g5-1': 'wt', 'g2-1': 'wt', 'g2-0': 's', 'g3-1': 'st', 'g1-1': 'w',
  'g1-0': 's', 'g6-0': 'st', 'g7-3': 'wt', 'g7-2': 's',
  'g2-3': 's', 'g1-2': 's', 'g1-3': 's', 'g6-1': 's', 'g6-3': 't', 'g7-0': 's', 'g7-1': 't',
};
const KEEP = new Set(['g3-2', 'g3-1', 'g4-0', 'g5-0', 'g5-1', 'g2-1', 'g2-0', 'g1-1', 'g6-0', 'g7-3', 'g7-2', 'g1-0']);
const T = [20, 18, 15]; // #14120F

const mjFile = (g, i) => fs.readdirSync(MJ).find(f => f.includes(JOB[g]) && f.endsWith('_' + i + '.jpg'));
function box(W, H, r) { let w = W, h = Math.round(W / r); if (h > H) { h = H; w = Math.round(H * r) } return { w, h } }
async function cornerMean(p) {
  const m = await sharp(p).metadata(); const c = Math.round(Math.min(m.width, m.height) * .05); const arr = [];
  for (const [l, t] of [[0, 0], [m.width - c, 0], [0, m.height - c], [m.width - c, m.height - c]]) {
    const s = await sharp(p).extract({ left: l, top: t, width: c, height: c }).stats(); arr.push(s.channels.slice(0, 3).map(x => x.mean))
  }
  return [0, 1, 2].map(i => arr.reduce((a, x) => a + x[i], 0) / 4)
}
async function encode(input, name, dir, kind, W, H, cropPos, isAI) {
  const r = RATIO[kind]; const cb = r ? box(W, H, r) : { w: W, h: H };
  let ws = SIZES[kind].filter(x => x <= cb.w); if (!ws.length || (cb.w - ws[ws.length - 1] > 80 && cb.w < SIZES[kind][SIZES[kind].length - 1])) ws.push(cb.w);
  ws = [...new Set(ws)].sort((a, b) => a - b);
  const jw = ws.includes(JPG[kind]) ? JPG[kind] : ws.reduce((a, b) => Math.abs(b - JPG[kind]) < Math.abs(a - JPG[kind]) ? b : a);
  const variants = [];
  for (const w of ws) {
    const h = Math.round(w * cb.h / cb.w);
    const base = () => sharp(input).rotate().toColorspace('srgb').resize({ width: w, height: h, fit: 'cover', position: cropPos || 'attention' });
    const q = kind === 'w' || kind === 'v' ? 55 : 52;
    const jobs = [['avif', s => s.avif({ quality: q, effort: 4 })], ['webp', s => s.webp({ quality: 78 })]];
    if (w === jw) jobs.push(['jpg', s => s.jpeg({ quality: 80, mozjpeg: true, progressive: true })]);
    for (const [ext, fn] of jobs) {
      const file = `${name}-${w}.${ext}`; const info = await fn(base()).toFile(`${dir}/${file}`);
      variants.push({ file: path.relative(OUT, `${dir}/${file}`), width: info.width, height: info.height, format: ext, bytes: info.size });
    }
  }
  return { crop: `${cb.w}x${cb.h}`, widths: ws, jpg: jw, variants };
}
(async () => {
  const t0 = Date.now(); const assets = [];
  // legacy
  for (const [id, L] of Object.entries(LEG)) {
    const src = `${IMG}/${id}.jpg`; const m = await sharp(src).metadata();
    for (const [k, o] of Object.entries(L.kinds)) {
      const kind = o.base || k; const name = `${id}-${k}`;
      const r = await encode(src, name, OUT + '/img/legacy', kind, m.width, m.height, o.position, false);
      assets.push({ id: `legacy/${name}`, source: 'LM BIJU (v17 images/)', sourceFile: `images/${id}.jpg`, sourceSize: `${m.width}x${m.height}`, kind, ratio: kind === 'v' ? 'original' : { p: '4:5', l: '3:2' }[kind], cropPosition: o.position || 'attention', ai: false, thirdParty: L.thirdParty || null, ...r });
    }
  }
  // MJ
  for (const [key, kinds] of Object.entries(MJS)) {
    const [g, i] = key.split('-'); const f = mjFile(g, i); const src = `${MJ}/${f}`; const m = await sharp(src).metadata();
    const cm = await cornerMean(src);
    const lin = cm.map((c, k) => { const t = c + 0.7 * (T[k] - c); const a = (255 - t) / (255 - c); return { a, b: t - a * c } });
    const corrected = await sharp(src).toColorspace('srgb').linear(lin.map(x => x.a), lin.map(x => x.b)).png().toBuffer();
    for (const kind of kinds) {
      const name = `mj-${key}-${kind}`;
      const r = await encode(corrected, name, OUT + '/img/mj', kind, m.width, m.height, null, true);
      assets.push({ id: `mj/${name}`, source: KEEP.has(key) ? 'Midjourney (12 retidas)' : 'Midjourney (aceitáveis, não retidas na 1.ª triagem)', sourceFile: `_research/mj-uploads/${f}`, sourceSize: `${m.width}x${m.height}`, kind, ratio: { w: '21:9', s: '3:2', t: '4:5' }[kind], ai: true, label: 'Imagem ilustrativa gerada por IA', blackPoint: { target: '#14120F', strength: 0.7, cornerBefore: '#' + cm.map(v => Math.round(v).toString(16).padStart(2, '0')).join('') }, ...r });
    }
  }
  // video: 48 graded frames (AVIF 1080 from stage B) + JPEG 720 fallback, poster, mobile loop
  const frames = { id: 'video/frames', source: 'hero.mp4 (filmagem própria) → 48 fotogramas', ai: false, variants: [] };
  for (let n = 1; n <= 48; n++) {
    const nn = String(n).padStart(3, '0'); const a = `${OLDV}/frame-${nn}-1080.avif`;
    fs.copyFileSync(a, `${OUT}/video/frame-${nn}-1080.avif`);
    const info = await sharp(a).resize({ width: 720 }).jpeg({ quality: 72, mozjpeg: true }).toFile(`${OUT}/video/frame-${nn}-720.jpg`);
    frames.variants.push({ file: `video/frame-${nn}-1080.avif`, bytes: fs.statSync(a).size }, { file: `video/frame-${nn}-720.jpg`, width: info.width, height: info.height, bytes: info.size });
  }
  assets.push(frames);
  for (const f of ['video-mobile-540.mp4', 'video-poster-1080.avif', 'video-poster-1080.webp', 'video-poster-1080.jpg', 'video-poster-540.avif', 'video-poster-540.jpg']) {
    fs.copyFileSync(`${OLDV}/${f}`, `${OUT}/video/${f}`);
  }
  assets.push({ id: 'video/loop', source: 'hero.mp4 (filmagem própria)', ai: false, variants: ['video-mobile-540.mp4', 'video-poster-1080.avif', 'video-poster-1080.webp', 'video-poster-1080.jpg', 'video-poster-540.avif', 'video-poster-540.jpg'].map(f => ({ file: 'video/' + f, bytes: fs.statSync(`${OUT}/video/${f}`).size })) });
  const man = { generated: new Date().toISOString(), pipeline: 'sRGB · metadados removidos · AVIF + WebP em todas as larguras · 1 JPEG de recurso', count: assets.length, assets };
  fs.writeFileSync(OUT + '/manifest.json', JSON.stringify(man, null, 1));
  const files = assets.reduce((a, x) => a + x.variants.length, 0), bytes = assets.reduce((a, x) => a + x.variants.reduce((s, v) => s + (v.bytes || 0), 0), 0);
  console.log(`assets ${assets.length} · files ${files} · ${(bytes / 1e6).toFixed(1)} MB · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
