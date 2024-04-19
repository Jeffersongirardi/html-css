let paragrafo = document.querySelector('#para1');
paragrafo.addEventListener('mouseover', mudaverde);
paragrafo.addEventListener('mouseout', mudavermelho);

function mudaverde() {
    paragrafo.style.background='green';
    }
function mudavermelho() {
    paragrafo.style.background='red';
}
