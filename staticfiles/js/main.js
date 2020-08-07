setTimeout(function(){
    $('#message').fadeOut('slow');
},3000);

$('#form1 select').on('change', function() {
    this.form.submit();
});