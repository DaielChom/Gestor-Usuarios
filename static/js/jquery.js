(function(){

  //Cuando el boton consultar es oprimido se dirige a una nueva direccion
  $('#consultar').on('click',(ev)=>{
    cedula = document.getElementById("cedula").value
    $('#cedula').attr('disable')
    window.location = "/usuarios/" + cedula
    })

  //Accion al ser orpimido el boton listo
  $('#listo').on('click',(ev)=>{
    window.location = "/usuarios"
    })

  //Al oprimir el boton crear se agregan y remueven algunas clases de CSS
  $('#crear').on('click',(ev)=>{
    $('#check').removeClass('hidden')
    $('#crear').addClass('hidden')
    $('#consultar').addClass('hidden')
    $('.labelForm').removeClass('hidden')
    $('.inputForm').removeClass('hidden').attr('required')
    $('#estilo-form').addClass('ancho-consulta')
    $('.material-icons').removeClass('hidden')
    })

  //Al oprimir el boton modificar llama la funcion ajax
  $('#modificar').on('click',(ev)=>{
    cedula = $('#cedula').val()
    respuesta = ajax('PUT', cedula)
    //Avisa el exito --Replantear forma de mostrar los avisos--
    //NOTA: Se pdoria solucionar mandando el mensage en return y haciendo el flash(message) cada vez que entre a usuarios
    window.location = "/usuarios/" + cedula
    })

  //Funcion para la peticion de eliminar
  $('#eliminar').on('click',(ev)=>{
    cedula = $('#cedula').val()
    respuesta = ajax('DELETE', cedula)
    window.location = "/usuarios"
  })

  //Temporizador para que los mensajes flash se oculten
  $(document).ready(function(){
    setTimeout(function() {
      $(".flashes").fadeOut(1500);
    },2000);
      });

  //funcion AJAX
  function ajax(metodo, cedula){

    //funcion ajax
    $.ajax({
      url:'/usuarios/' + cedula,
      data: $('form').serialize(),
      type: metodo,
      success: function(response){ console.log(response);},
      error: function(error){console.log(error);}
      });
    }

})();
