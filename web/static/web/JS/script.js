$('.fecha_sel').on('change',
    function(){
        var res = $('.fecha_sel').val();
        document.getElementById('fecha_reserva').innerHTML = res;
        
});

$(document).ready(function() {
    $('#formHora input').on('change', function() {
        var horaSeleccionada = $('input[name=hora]:checked', '#formHora').val();

        $('#hora_reserva').text(horaSeleccionada);
    });
});




