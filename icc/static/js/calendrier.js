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
function requeteAjax(day) {
    var xhr = new XMLHttpRequest()
    var getm = day.getMonth()+1

    xhr.open('GET', '/reservations/ajax-' + day.getDate() + '-' + getm + '-' + day.getFullYear() + '/', false)

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {

            // result.innerHTML = ''
            if (xhr.status === 200) {
                // var d = day.getDate()
                // var m = day.getMonth()
                // var y = day.getFullYear()
                // result.innerHTML = day
                var jsonResponse = JSON.parse(xhr.responseText)
                console.log('response totale! ___=>', jsonResponse)
                // Object.entries(jsonResponse).forEach(
                //     ([key, value]) => console.log(key, value)
                // );
                var matin = []
                var apresmidi = []
                for (var i = 0; i < jsonResponse.length; i++) {
                    // console.log(i, jsonResponse[i])
                    if (jsonResponse[i]['fields'].heure <= '12:00:00'){
                        // console.log('c\'est le matin')
                        matin.push(jsonResponse[i])
                    } else {
                        // console.log('c\'est l\'apres midi')
                        apresmidi.push(jsonResponse[i])
                    }
                }
                effacer()
                afficher(matin, apresmidi)

                // console.log('list_matin', matin)
                // console.log('list_apresmidi', apresmidi)
                // console.log(xhr.responseText)
                // result.innerHTML = xhr.responseText
                // console.log('voici la date du jour', d,m,y)
            } else {
                // console.log('ça marche pas!')
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
    // var r_matin = document.getElementsByName('r_matin')
    // console.log('r_matin: ', r_matin)
});

subDay.addEventListener("click", function () {
    compteur = compteur - 1;
    console.log(compteur);
    var day = dateDuJour.addDays(compteur)
    affichage(day, message);
    requeteAjax(day)
});