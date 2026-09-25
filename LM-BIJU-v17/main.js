/* LM BIJU v16 · shared behaviours */
(function(){
  "use strict";
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* sticky header shadow */
  var top = document.getElementById('top');
  if (top) {
    var onScroll = function(){ top.classList.toggle('stuck', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }

  /* mobile nav */
  var burger = document.getElementById('burger'), mnav = document.getElementById('mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function(){
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      mnav.classList.toggle('open', !open);
    });
    mnav.addEventListener('click', function(e){
      if (e.target.tagName === 'A') { burger.setAttribute('aria-expanded','false'); mnav.classList.remove('open'); }
    });
  }

  /* hero video: graceful fallback + reduced-motion pause + toggle */
  var hero = document.getElementById('hero');
  var vid = document.getElementById('heroVid');
  var muteBtn = document.getElementById('hMute'), muteTx = document.getElementById('hMuteTx');
  function videoOff(){ if(hero){hero.classList.add('no-video');} if(muteBtn){muteBtn.style.display='none';} }
  if (hero && vid) {
    vid.addEventListener('error', videoOff, true);
    var src = vid.querySelector('source');
    if (src) src.addEventListener('error', videoOff);
    if (reduce) { vid.pause(); vid.removeAttribute('autoplay'); if(muteTx) muteTx.textContent='Reproduzir'; }
    var p = vid.play ? vid.play() : null;
    if (p && p.catch) p.catch(function(){});
    if (muteBtn) muteBtn.addEventListener('click', function(){
      if (vid.paused) { vid.play(); muteTx.textContent='Pausar'; } else { vid.pause(); muteTx.textContent='Reproduzir'; }
    });
    /* 标题逐行揭示 */
    requestAnimationFrame(function(){ setTimeout(function(){ hero.classList.add('in'); }, 120); });
    /* 底栏亮点轮播（仅文案） */
    var caps = (document.getElementById('hCaps') || {}).textContent;
    var hCap = document.getElementById('hCap');
    var dots = [].slice.call(document.querySelectorAll('#dots button'));
    if (caps && hCap && dots.length) {
      caps = caps.split('|');
      var cur = 0, timer = null;
      var go = function(i){
        var n = ((i % caps.length) + caps.length) % caps.length;
        if (n === cur) return;
        dots[cur].setAttribute('aria-selected','false');
        cur = n; dots[cur].setAttribute('aria-selected','true');
        hCap.style.opacity = 0;
        setTimeout(function(){ hCap.textContent = caps[cur]; hCap.style.opacity = 1; }, 220);
      };
      hCap.style.transition = 'opacity .22s';
      var auto = function(){ if(reduce) return; clearInterval(timer); timer = setInterval(function(){ go(cur+1); }, 6000); };
      dots.forEach(function(b,i){ b.addEventListener('click', function(){ go(i); auto(); }); });
      auto();
    }
  }

  /* catalog filter chips */
  var chips = [].slice.call(document.querySelectorAll('.chips button'));
  var cards = [].slice.call(document.querySelectorAll('#catGrid .pcard'));
  if (chips.length && cards.length) {
    chips.forEach(function(ch){
      ch.addEventListener('click', function(){
        chips.forEach(function(c){ c.classList.remove('on'); });
        ch.classList.add('on');
        var f = ch.getAttribute('data-f');
        cards.forEach(function(cd){
          var show = (f === 'all') || (cd.getAttribute('data-cat') === f);
          cd.style.display = show ? '' : 'none';
        });
      });
    });
  }

  /* quick-view */
  var mask = document.getElementById('qvMask');
  if (mask) {
    var qImg = document.getElementById('qvImg'), qName = document.getElementById('qvName'),
        qSku = document.getElementById('qvSku'), qRrp = document.getElementById('qvRrp'),
        qMats = document.getElementById('qvMats'), qQty = document.getElementById('qvQty'),
        qX = document.getElementById('qvX'), qty = 1, lastFocus = null;
    var openQV = function(card){
      lastFocus = card;
      qImg.src = card.getAttribute('data-img');
      qImg.alt = card.getAttribute('data-name');
      qName.textContent = card.getAttribute('data-name');
      qSku.textContent = 'REF ' + card.getAttribute('data-sku');
      qRrp.textContent = card.getAttribute('data-rrp');
      qMats.innerHTML = '';
      (card.getAttribute('data-mats') || '').split('|').forEach(function(m){
        if (!m) return;
        var li = document.createElement('li'); li.textContent = m; qMats.appendChild(li);
      });
      qty = 1; qQty.textContent = '1';
      mask.classList.add('open');
      document.body.style.overflow = 'hidden';
      qX.focus();
    };
    var closeQV = function(){
      mask.classList.remove('open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };
    [].forEach.call(document.querySelectorAll('.pcard[data-name]'), function(c){
      c.addEventListener('click', function(ev){ ev.preventDefault(); openQV(c); });
    });
    qX.addEventListener('click', closeQV);
    mask.addEventListener('click', function(e){ if (e.target === mask) closeQV(); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && mask.classList.contains('open')) closeQV(); });
    var qm = document.getElementById('qvMinus'), qp = document.getElementById('qvPlus');
    if (qm) qm.addEventListener('click', function(){ if(qty>1){qty--; qQty.textContent=qty;} });
    if (qp) qp.addEventListener('click', function(){ if(qty<99){qty++; qQty.textContent=qty;} });
  }

  /* reveal on scroll */
  var items = document.querySelectorAll('.rv');
  if (reduce || !('IntersectionObserver' in window)) {
    [].forEach.call(items, function(el){ el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting) {
          var sibs = e.target.parentNode ? e.target.parentNode.children : [e.target];
          var k = [].indexOf.call(sibs, e.target);
          e.target.style.transitionDelay = Math.min(k,6) * 60 + 'ms';
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, {threshold:.08, rootMargin:'0px 0px -40px 0px'});
    [].forEach.call(items, function(el){ io.observe(el); });
  }
})();
