// Affiche la date

function affichage(n) {
    y = n.getFullYear();
    m = n.toLocaleString('default', {month: 'long'})
    d = n.getDate();
    j = n.toLocaleDateString('default', {weekday: 'long'});
    //document.getElementById("date").innerHTML = j.replace(/^\w/, (c) => c.toUpperCase()) + ", " + d + " " + m + " " + y;
    //{#    remplacer le noeud p #}
    var date = document.createElement("p");
    date.innerHTML = j + ", " + d + " " + m + " " + y;;
    document.body.appendChild(date);
}