(function(window, document, undefined){

// code that should be taken care of right away

window.onload = init;

  function init(){
    const infoIcon = document.getElementById("infoIcon")
    const modal = document.getElementById("modal")


    function open() {
       modal.setAttribute("style", "display:block;")
       console.log('fffff')
    }

    function close() {
       modal.setAttribute("style", "display:none;")
    }

infoIcon.addEventListener("mouseover", open);
infoIcon.addEventListener("mouseout", close);

  }

})(window, document, undefined);

