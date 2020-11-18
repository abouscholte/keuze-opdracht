// function for opening and closing navbar on mobile devices

function navbarToggle(el) {
  var navigation = el.getAttribute('data-navigation');
  var navigationEl = document.getElementById(navigation);

  el.classList.toggle('focussed');
  navigationEl.classList.toggle('visible');
}


// auto-hide alerts after 15 seconds

var alert = document.getElementById('page-alert');

if (alert) {
  setTimeout(function() {
    alert.classList.add('invisible');
  }, 15000);
}