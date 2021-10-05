$(document).ready(function(){
    $('#datanascimento').mask('00/00/0000');
    $('#telefone').mask('(00)00000-0000');
    $('#cpf').mask('000.000.000-00');
})


document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: "pt-br",
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
        navLinks: true, // can click day/week names to navigate views
        businessHours: true, // display business hours
        editable: true,
        selectable: true,
        events: [
            {
                id : '1',
                title: "Corte Simples",
                start: "2021-10-11T15:00:00",
                end: "2021-10-11T16:00:00",
            }
        ],
        eventClick: function(info) {
            info.jsEvent.preventDefault();

            $('#visualizar #id').text(info.event.id)
            $('#visualizar #title').text(info.event.title)
            $('#visualizar #start').text(info.event.start.toLocaleString())
            $('#visualizar #end').text(info.event.end.toLocaleString())
            $('#visualizar').modal("show")
          },
        select: function(info){
            // alert("Início " + info.start.toLocaleString())
            $("#cadastrar #start").val(info.start.toLocaleString())
            $("#cadastrar #end").val(info.end.toLocaleString())
            $("#cadastrar").modal("show")
        },
        });
    calendar.render();
});


function DataHora(evento, objeto){
	var keypress=(window.event) ? event.keyCode:evento.which;
	campo = eval (objeto);
	if (campo.value == '00/00/0000 00:00:00')
	{
		campo.value=""
	}
 
	caracteres = '0123456789';
	separacao1 = '/';
	separacao2 = ' ';
	separacao3 = ':';
	conjunto1 = 2;
	conjunto2 = 5;
	conjunto3 = 10;
	conjunto4 = 13;
	conjunto5 = 16;
	if ((caracteres.search(String.fromCharCode (keypress))!=-1) && campo.value.length < (19))
	{
		if (campo.value.length == conjunto1 )
		campo.value = campo.value + separacao1;
		else if (campo.value.length == conjunto2)
		campo.value = campo.value + separacao1;
		else if (campo.value.length == conjunto3)
		campo.value = campo.value + separacao2;
		else if (campo.value.length == conjunto4)
		campo.value = campo.value + separacao3;
		else if (campo.value.length == conjunto5)
		campo.value = campo.value + separacao3;
	}
	else
		event.returnValue = false;
};

$(document).ready(function(){
    $("#addEvent").on("submit", function(event){
        event.preventDefault();
        $.ajax({
            method: "POST",
            url: '/',
            data: new FormData(this),
            contentType: false,
            processData: false,
            success: function(retorna){
                     
            }
        })
    });
});