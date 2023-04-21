// aca al seleccionar una opcion en el select box se llena el otro select
function llenar_segundo_select(){

    //se apunta a los select
    primer_select = document.getElementById('usuario');
    segundo_select = document.getElementById('amigo');
    //se vacia el segundo select
    segundo_select.innerText = null;

    //se llena el segundo select
    for (i=0;i<primer_select.length;i++)
    {
       if (primer_select.options[i].value != primer_select.options[primer_select.selectedIndex].value)
       {

           let opt = document.createElement("option");
           opt.value= primer_select.options[i].value;
           opt.innerHTML = primer_select.options[i].innerHTML;
           segundo_select.appendChild(opt)
       }
    }
}