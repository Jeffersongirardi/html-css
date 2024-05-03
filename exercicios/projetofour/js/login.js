const passwordInput = document.getElementById('senha');
const passwordStrength = document.getElementById('password-strength');

passwordInput.addEventListener('input', function() {
    const password = passwordInput.value;
    const result = zxcvbn(password);
    const score = result.score;

    switch (score) {
        case 0:
        case 1:
            passwordStrength.textContent = 'Força da Senha: Fraca';
            passwordStrength.className = 'password-strength weak';
            break;
        case 2:
            passwordStrength.textContent = 'Força da Senha: Regular';
            passwordStrength.className = 'password-strength good';
            break;
        case 3:
        case 4:
            passwordStrength.textContent = 'Força da Senha: Forte';
            passwordStrength.className = 'password-strength strong';
            break;
    }
});
