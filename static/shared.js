var backdrop = document.querySelector(".backdrop");
var toggleButton = document.querySelector(".togglebutton");
var mobileNav = document.querySelector(".mobilenav");
var modal = document.querySelector(".modal");


backdrop.addEventListener("click", function() {
    mobileNav.style.display = 'none';
    backdrop.style.display = 'none';
    this.closeModal();
});

toggleButton.addEventListener("click", function() {
    mobileNav.style.display= 'block';
    backdrop.style.display= 'block';
});

function closeModal(){
    backdrop.style.display = 'none';
}




