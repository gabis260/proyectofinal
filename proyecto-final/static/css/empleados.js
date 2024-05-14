function obtenerEmpleados() {
    fetch('/api/empleados')
      .then(response => response.json())
      .then(data => {
        // Actualizar la tabla de empleados con los datos obtenidos
        const tbody = document.getElementById('empleados-tabla').getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';
        data.forEach(empleado => {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td>${empleado.id}</td>
            <td>${empleado.nombre}</td>
            <td>${empleado.email}</td>
            <!-- Agrega más columnas según tus necesidades -->
          `;
          tbody.appendChild(row);
        });
      })
      .catch(error => console.error('Error al obtener empleados:', error));
  }
  
  window.onload = obtenerEmpleados;


  function crearEmpleado() {
    const nombreInput = document.getElementById('nombre');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
  
    const nuevoEmpleado = {
      nombre: nombreInput.value,
      email: emailInput.value,
      password: passwordInput.value
    };
  
    fetch('/api/empleados', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(nuevoEmpleado)
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.mensaje);
      nombreInput.value = '';
      emailInput.value = '';
      passwordInput.value = '';
      obtenerEmpleados(); 
    })
    .catch(error => {
      console.error('Error al crear empleado:', error);
    });
  }


