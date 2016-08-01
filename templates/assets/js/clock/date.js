var monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
];
var dayNames = ["Dom, ", "Lun, ", "Mar, ", "Mie, ", "Jue, ", "Vie, ", "Sab, "]

var newDate = new Date();
newDate.setDate(newDate.getDate() + 1);
$('#Date').html(dayNames[newDate.getDay()] + " " + newDate.getDate() + ' ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());
