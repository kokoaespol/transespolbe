var fila=2
$(document).ready(function(){
  $("td").click(function(){
    $(this).hide()
  })
})

function agregar(){
  var tr,td;
  tr = document.all.tabla.insertRow();
  td = tr.insertCell();
  td.innerHTML = "<td id='"+ fila.toString() +"1'>" +fila.toString() +"1</td>"
  td = tr.insertCell();
  td.innerHTML = "<td id='"+ fila.toString() +"2'>"+ fila.toString() +"2</td>"
  td = tr.insertCell();
  td.innerHTML = "<td id='"+ fila.toString() +"3'>"+ fila.toString() +"3</td>"
  td = tr.insertCell();
  td.innerHTML = "<td id='"+ fila.toString() +"4'>"+ fila.toString() +"4</td>"
  fila++;
}
function borrar(){
  ultima = document.all.tabla.rows.length - 1;
  document.all.tabla.deleteRow(ultima);
}
