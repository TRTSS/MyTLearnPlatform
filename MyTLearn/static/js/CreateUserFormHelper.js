let usernameInput = document.querySelector('#id_username');
let firstnameInput = document.querySelector('#id_firstname');
let surnameInput = document.querySelector('#id_surname');
let passwordInput = document.querySelector('#id_password');


let randomstring = Math.random().toString(36).slice(-8);
passwordInput.value = randomstring;

passwordInput.setAttribute('readonly', true)
passwordInput.type = 'password';
usernameInput.setAttribute('readonly', true)

function translit(word) {
    var answer = '';
    var converter = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Sch', 'Ь': '', 'Ы': 'Y', 'Ъ': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    };
    for (var i = 0; i < word.length; ++i) {
        if (converter[word[i]] == undefined) {
            answer += word[i];
        } else {
            answer += converter[word[i]];
        }
    }
    return answer;
}

firstnameInput.oninput = function () {
    let f = firstnameInput.value[0];
    if (firstnameInput.value.length === 0) {
        f = '';
    }
    usernameInput.value = translit(f + "_" + surnameInput.value);
}

surnameInput.oninput = function () {
    let f = firstnameInput.value[0];
    if (firstnameInput.value.length === 0) {
        f = '';
    }
    usernameInput.value = translit(f + "_" + surnameInput.value);
}