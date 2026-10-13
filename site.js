'use strict';
const play = document.getElementById('video-load');
if (play) play.addEventListener('click', () => {
  const frame = document.createElement('iframe');
  frame.src = 'https://www.youtube-nocookie.com/embed/STcmVYqeqQ8?autoplay=1&rel=0';
  frame.title = 'XPPanelsVR for Quest demonstration';
  frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
  frame.referrerPolicy = 'strict-origin-when-cross-origin';
  frame.allowFullscreen = true;
  document.getElementById('video-shell').replaceChildren(frame);
  frame.focus();
});
