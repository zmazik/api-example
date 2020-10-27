onload = get_neko

function get_neko() {
    fetch('https://nekos.life/api/neko')
        .then(response => response.json())
        .then(val => $('#img').attr('src', val['neko']))
}
