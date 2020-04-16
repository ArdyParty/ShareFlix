function navSlide() {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');
  
  
  burger.addEventListener('click', ()=> {
    //toggle Nav
    nav.classList.toggle('nav-active');

    //animate links
    navLinks.forEach((link, index)=> {
      if(link.style.animation) {
        link.style.animation = '';
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 + 0.2}s`
      }
    });

    //burger animation
    burger.classList.toggle('open')
  });
}
navSlide();


// function modal() {
//   const buttonEl = document.getElementById('btn-1');

//   buttonEl.addEventListener('click', ()=> {
//     buttonEl.style
//   });
// }

// modal();

// Get the modal
const modal = document.querySelector("#myModal");
// Get the button that opens the modal
const btn = document.getElementById("myBtn");
// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];
// When the user clicks on the button, open the modal

btn.addEventListener('click', ()=>{
  modal.style.display = "block";
});

// When the user clicks on <span> (x), close the modal

span.addEventListener('click', ()=>{
  modal.style.display = "none";
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}