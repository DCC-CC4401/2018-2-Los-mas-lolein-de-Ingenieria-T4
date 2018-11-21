function jumpTo(anchor) {
	document.getElementById(anchor).scrollIntoView();
}

/* Home page */

function addCoev() {
    document.getElementById("add-coev-form").style.display = "block";
    document.getElementById("add-curso-form").style.display = "none";
    document.getElementById("add-coev-btn").classList.add("active");
    document.getElementById("add-curso-btn").classList.remove("active");
}

function addCurso() {
    document.getElementById("add-coev-form").style.display = "none";
    document.getElementById("add-curso-form").style.display = "block";
    document.getElementById("add-coev-btn").classList.remove("active");
    document.getElementById("add-curso-btn").classList.add("active");
}

function cancelAdd() {
    document.getElementById("add-coev-form").style.display = "none";
    document.getElementById("add-curso-form").style.display = "none";
    document.getElementById("add-coev-btn").classList.remove("active");
    document.getElementById("add-curso-btn").classList.remove("active");
}

/* Perfil */

function changePass() {
    document.getElementById("cambiar-contrasena").style.display = "block";
    var x = document.querySelectorAll('[id^="notas-resumen-"]');
    var i;
    for(i=0; i<x.length; i++){
        x[i].style.display = "none"
    }
    document.getElementById("notas-placeholder").style.display = "none";
    document.getElementById("change-pass-btn").classList.add("active");
    document.getElementById("row-btn").classList.remove("active");
}

function showNotas(curso_pk) {
    var x = document.querySelectorAll('[id^="notas-resumen-"]');
    var i;
    for(i=0; i<x.length; i++){
        x[i].style.display = "none"
    }
    document.getElementById("cambiar-contrasena").style.display = "none";
    document.getElementById("notas-resumen-"+curso_pk).style.display = "block";
    document.getElementById("notas-placeholder").style.display = "none";

    var y = document.querySelectorAll('[id^="row-btn-"]');
    var j;
    for(j=0; j<y.length; j++){
        y[j].classList.remove("active");
    }
    document.getElementById("row-btn-"+curso_pk).classList.add("active");
    var changePass = document.getElementById("change-pass-btn");
    if (changePass !== null) changePass.classList.remove("active");
}

function cancelPass() {
    document.getElementById("cambiar-contrasena").style.display = "none";
    document.getElementById("notas-resumen").style.display = "none";
    document.getElementById("change-pass-btn").classList.add("active");
    document.getElementById("notas-placeholder").style.display = "block";
}

/* Gestión Curso */

function showGestionEstudiante() {
    document.getElementById("gestion-grupo").style.display = "none";
    document.getElementById("gestion-estudiante").style.display = "block";
    document.getElementById("gestion-placeholder").style.display = "none";
    document.getElementById("active-estudiante").classList.add("active");
    document.getElementById("active-grupo").classList.remove("active");
}

function showGestionGrupo() {
    document.getElementById("gestion-grupo").style.display = "block";
    document.getElementById("gestion-estudiante").style.display = "none";
    document.getElementById("gestion-placeholder").style.display = "none";
    document.getElementById("active-grupo").classList.add("active");
    document.getElementById("active-estudiante").classList.remove("active");
}