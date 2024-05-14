function iniciarSesion() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
   
    fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error al iniciar sesión:', error);
    });
  }
  
  function pagarNomina() {
    fetch('/api/nomina/pago', {
      method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error al pagar la nómina:', error);
    });
  }