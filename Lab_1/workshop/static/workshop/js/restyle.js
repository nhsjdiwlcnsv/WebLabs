const fontSizeCheckbox = document.getElementById('fontSizeCheckbox');
const fontSizeInput = document.getElementById('fontSizeInput');
const textColorCheckbox = document.getElementById('textColorCheckbox');
const header = document.getElementById('header');

fontSizeCheckbox.addEventListener(
    'change',
    function () {
        if (this.checked) {
            let inp = document.createElement('input')

            inp.id = 'fontSizeInput'
            inp.type =  "number"
            inp.min = '10'
            inp.max = '1000'
            inp.step = '1'

            document.getElementById("fontSizeContainer").appendChild(inp);
            inp.addEventListener('input', function () {document.body.style.fontSize = this.value + 'px'})
        } else {
            let element = document.getElementById('fontSizeInput');
            element.remove()
        }
    });

textColorCheckbox.addEventListener(
    'change',
    function () {
        if (this.checked) {
            let inp = document.createElement('input')

            inp.id = 'textColorPicker'
            inp.type = "color"

            document.getElementById("textColorContainer").appendChild(inp);
            inp.addEventListener('input', function () {document.body.style.color = this.value})
        } else {
            let element = document.getElementById('textColorPicker');
            element.remove()
        }
    });

bgColorCheckbox.addEventListener(
    'change',
    function () {
        if (this.checked) {
            let inp = document.createElement('input')

            inp.id = 'bgColorPicker'
            inp.type = "color"

            document.getElementById("bgColorContainer").appendChild(inp);
            inp.addEventListener('input', function () {document.body.style.backgroundColor = this.value})
        } else {
            let element = document.getElementById('bgColorPicker');
            element.remove()
        }
    });