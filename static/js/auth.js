document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('password');
    const progressBar = document.querySelector('.password-strength .progress-bar');
    const strengthText = document.getElementById('strengthText');
    
    passwordInput.addEventListener('input', function() {
        const strength = calculatePasswordStrength(this.value);
        progressBar.style.width = strength.percentage + '%';
        progressBar.setAttribute('aria-valuenow', strength.percentage);
        strengthText.textContent = strength.label;
    });
    
    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength += 25;
        if (password.match(/[a-z]/)) strength += 25;
        if (password.match(/[A-Z]/)) strength += 25;
        if (password.match(/[0-9]/)) strength += 25;
        
        let label = 'Very Weak';
        if (strength >= 25) label = 'Weak';
        if (strength >= 50) label = 'Medium';
        if (strength >= 75) label = 'Strong';
        if (strength === 100) label = 'Very Strong';
        
        return { percentage: strength, label: label };
    }
});
