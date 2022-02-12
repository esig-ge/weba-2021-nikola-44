// {# Stocke les flèches du calendrier dans des variables #}
var addDay = document.querySelector('#addDay');
var subDay = document.querySelector('#subDay');
// Récupère la div pour pouvoir insérer la date
var div = document.querySelector("#date-div");
// Crée un élément p et l'ajoute à la div
var p = document.createElement("p");
div.appendChild(p);

function message() {
    var alerte = document.createElement("p");
    alerte.setAttribute("id", "alerte");
    alerte.style.backgroundColor = "red"
    alerte.style.color = "white"
    alerte.style.border = "solid 3px black"

    if (compteur < 0) {
        div.appendChild(alerte);
        alerte.innerHTML = "La date est déjà passée!";
        console.log("La date est déjà passée!")
    }
    if (compteur > 29) {
        div.appendChild(alerte);
        alerte.innerHTML = "Il est impossible de reserver 30 jours à l'avance!";
        console.log("Il est impossible de reserver 30 jours à l'avance!")
    }
}

function affichage(date, callback) {
    annee = date.getFullYear();
    mois = date.toLocaleString('default', {month: 'long'});
    jourEnChiffres = date.getDate();
    jourEnLettres = date.toLocaleDateString('default', {weekday: 'long'});
    p.innerHTML = jourEnLettres.replace(/^\w/, (c) => c.toUpperCase()) + ", " + jourEnChiffres + " " + mois + " " + annee;
    console.log(date);
    if (div.childNodes.length > 2) {
        div.removeChild(div.lastChild)
    }
    callback();
}

// {# Crée une fonction qui ajoute le nombre de jour en paramètre à la date du jour #}
Date.prototype.addDays = function (days) {
    var date = new Date();
    date.setDate(date.getDate() + days);
    return date;
};

// {# Initialise la date du jour du système et l'affiche #}
dateDuJour = new Date();
affichage(dateDuJour, message);

//Ajax
// var formsubday = document.getElementById('form-subday')
// var formaddday = document.getElementById('form-addday')
// // var csrf = document.getElementsByName('csrfmiddelwaretoken')
// // console.log('csrf', csrf)
//
// formsubday.addEventListener('submit', (e)=>{
//     e.preventDefault()
//     requeteAjax()
//     return false
// }
//     )
// formaddday.addEventListener('submit', requeteAjax)

function requeteAjax(day) {
    var result = document.getElementById('row-date').appendChild(document.createElement('p'))
    result.setAttribute('id', 'result')
    var xhr = new XMLHttpRequest()
    var getm = day.getMonth()+1

    xhr.open('GET', '/reservations/ajax-' + day.getDate() + '-' + getm + '-' + day.getFullYear() + '/', true)

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {

            result.innerHTML = ''
            if (xhr.status === 200) {
                var d = day.getDate()
                var m = day.getMonth()
                var y = day.getFullYear()
                result.innerHTML = day
                console.log('voici la date du jour', d,m,y)
            } else {
                console.log('ça marche pas!')
            }
        }
    }
    xhr.send()
}

//Fin ajax

// Compte le decalage en jour avec la date d'aujourd'hui
var compteur = 0;

addDay.addEventListener("click", function () {
    compteur = compteur + 1;
    console.log(compteur);
    var day = dateDuJour.addDays(compteur)
    affichage(day, message);
    requeteAjax(day)
});

subDay.addEventListener("click", function () {
    compteur = compteur - 1;
    console.log(compteur);
    var day = dateDuJour.addDays(compteur)
    affichage(day, message);
    requeteAjax(day)
});