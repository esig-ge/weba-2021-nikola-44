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
    // console.log('maaaatiiiin', matin)

    for (var i = 0; i < matin.length; i++) {
        // console.log(matin[i])
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
        var path1 = document.createElement('path')
        path1.setAttribute('d','M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z')
        svg.appendChild(path1)
        var path2 = document.createElement('path')
        path2.setAttribute('fill-rule','evenodd')
        path2.setAttribute('d','M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z')
        svg.appendChild(path2)

        var d3 = document.createElement('div')
        d3.setAttribute('id','div-heure')
        d3.setAttribute('class','heure fw-bold mt-5')
        d3.innerHTML = matin[i]['fields'].heure.substring(0,matin[i]['fields'].heure.length - 3)
        d1.appendChild(d3)
    }

    var rowapresmidi = document.getElementById('row-apresmidi')

    for (var i = 0; i < apresmidi.length; i++) {
        var d1 = document.createElement('div')
        d1.setAttribute('id', 'div-apresmidi')
        d1.setAttribute('class', 'col-sm-2 text-center p-1 justify-content-center m-1 reservationr modele')
        rowapresmidi.appendChild(d1)
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
        var path1 = document.createElement('path')
        path1.setAttribute('d','M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z')
        svg.appendChild(path1)
        var path2 = document.createElement('path')
        path2.setAttribute('fill-rule','evenodd')
        path2.setAttribute('d','M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z')
        svg.appendChild(path2)

        var d3 = document.createElement('div')
        d3.setAttribute('id','div-heure')
        d3.setAttribute('class','heure fw-bold mt-5')
        d3.innerHTML = apresmidi[i]['fields'].heure.substring(0,apresmidi[i]['fields'].heure.length - 3) // + ' - ' + apresmidi[i]['fields'].heure_fin
        d1.appendChild(d3)
    }
}