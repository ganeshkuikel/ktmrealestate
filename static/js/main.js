setTimeout(function(){
    $('#message').fadeOut('slow');
},3000);

$('#form1 select').on('change', function() {
    this.form.submit();
});


const drop_btn = document.querySelector(".drop-btn span");
const tooltip = document.querySelector(".tooltip");
const menu_wrapper = document.querySelector(".wrapper");
const menu_bar = document.querySelector(".menu-bar");
drop_btn.onclick = (()=>{
menu_wrapper.classList.toggle("show");
tooltip.classList.toggle("show");