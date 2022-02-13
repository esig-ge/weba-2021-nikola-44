function effacer(){
    document.getElementById('row-apresmidi')
        .querySelectorAll('#div-apresmidi')
        .forEach(item => {
        item.remove()
    })
    document.getElementById('row-matin')
        .querySelectorAll('#div-matin')
        .forEach(item => {
        item.remove()
    })
}

function afficher(matin, apresmidi){
    var rowmatin = document.getElementById('row-matin')
    console.log('maaaatiiiin', matin)

    // matin.forEach(item => {
    //     var d1 = document.createElement('div')
    //     d1.setAttribute('id', 'div-matin')
    //     d1.setAttribute('class', 'col-sm-2 text-center p-1 justify-content-center m-1 reservationr modele')
    // })
    for (var i = 0; i < matin.length; i++) {
        console.log(matin[i])
        var d1 = document.createElement('div')
        d1.setAttribute('id', 'div-matin')
        d1.setAttribute('class', 'col-sm-2 text-center p-1 justify-content-center m-1 reservationr modele')
        rowmatin.appendChild(d1)
        var d2 = document.createElement('div')
        d2.setAttribute('class', 'modif align-self-start')
        d2.setAttribute('data-bs-toggle', 'modal')
        d2.setAttribute('data-bs-target', '#exampleModal')
        d1.appendChild(d2)
        var svg = document.createElement('svg')
        svg.setAttribute('xmlns','http://www.w3.org/2000/svg')
        svg.setAttribute('width','24')
        svg.setAttribute('height','24')
        svg.setAttribute('fill','currentColor')
        svg.setAttribute('class','bi bi-pencil-square float-end')
        svg.setAttribute('viewBox','0 0 16 16')
        d2.appendChild(svg)


        var d3 = document.createElement('div')
        d3.setAttribute('id','div-heure')
        d3.setAttribute('class','heure fw-bold mt-5')
        d3.innerHTML = matin[i]['fields'].heure
        console.log(matin[i]['fields'].heure)
        d1.appendChild(d3)
    }
}