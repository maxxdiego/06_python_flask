// Enviando uma requisição GET para API para listar todos os games

axios.get("http://localhost:5000/games").then((response) => {
    const games = response.data
    const listGames = document.getElementById("games")

    games.forEach((game) => {
      let item = document.createElement("li")

      item.innerHTML = `<h4>${game.titulo}</h4>
        <p>Descrição: ${game.descricao}</p> 
        <p>Ano: ${game.ano}</p>
        <p>ID: ${game._id}</p>`

        var deleteBtn = document.createElement("button")
        deleteBtn.innerHTML = "Deletar"
        deleteBtn.classList.add("btn", "btn-danger", "mb-3")

        var editBtn = document.createElement("button")
        editBtn.innerHTML = "Editar"
        editBtn.classList.add("btn", "btn-warning", "mb-3")

        item.appendChild(deleteBtn)
        item.appendChild(editBtn)
        listGames.appendChild(item)
      })
    }).catch((error) => {
      console.log(error)
    })