function myFunction() {
  document.getElementById("hidden-nav").classList.toggle("show");
}

window.onclick = function(e) {
  if (!e.target.matches('.fa-bars')) {
  var myDropdown = document.getElementById("hidden-nav");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}