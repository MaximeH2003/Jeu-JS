document.addEventListener("DOMContentLoaded", function () {
  const btnRock = document.getElementById("btnRock");
  const btnSheet = document.getElementById("btnSheet");
  const btnCut = document.getElementById("btnCut");
  const maxPointsInput = document.getElementById("max-points-input");
  const resultContainer = document.getElementById("result-container");
  const choiceMessage = document.getElementById("choice-message");
  const scoresContainer = document.getElementById("scores-container");
  const WinnerContainer = document.getElementById("winner-players")
  const gameEndContainer = document.getElementById("game-end-container");
  const gameEndMessage = document.getElementById("game-end-message");
  const restartButton = document.getElementById("restart-button");

  let maxPoints = 0;
  let playerScore = 0;
  let computerScore = 0;
  let gameEnded = false;

  btnRock.addEventListener("click", function () {
    if (!gameEnded) playRound("pierre");
  });

  btnSheet.addEventListener("click", function () {
    if (!gameEnded) playRound("papier");
  });

  btnCut.addEventListener("click", function () {
    if (!gameEnded) playRound("ciseaux");
  });

  restartButton.addEventListener("click", function () {
    location.reload(); // Recharge la page pour recommencer une nouvelle partie
  });

  function playRound(playerChoice) {
    const computerChoice = getRandomChoice();
    const result = determineWinner(playerChoice, computerChoice);
    updateScores(result);
    displayResult(result, playerChoice, computerChoice);
  }

  function getRandomChoice() {
    const choices = ["pierre", "papier", "ciseaux"];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
  }

  function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
      return "égalité";
    } else if (
      (playerChoice === "pierre" && computerChoice === "ciseau") ||
      (playerChoice === "papier" && computerChoice === "pierre") ||
      (playerChoice === "ciseau" && computerChoice === "papier")
    ) {
      return "player";
    } else {
      return "computer";
    }
  }

  function updateScores(result) {
    if (result === "player") {
      playerScore++;
    } else if (result === "computer") {
      computerScore++;
    }

    scoresContainer.textContent = `Score: Player = ${playerScore} , Score : computer = ${computerScore}`;
    WinnerContainer.textContent = `Le gagnant est : ${result}`

    if (playerScore >= maxPoints || computerScore >= maxPoints) {
      endGame();
    }
  }

  function displayResult(result, playerChoice, computerChoice) {
    const choiceMessage = document.getElementById("choice-message");
    const resultContainer = document.getElementById("result-container");
    // Sélectionne tous les éléments avec la classe "displayResult"
    const displayResults = document.querySelectorAll('.displayResult');
    // Change la propriété visibility de ces éléments à "visible"
    displayResults.forEach(element => {
      element.style.visibility = "visible";
    });
  
    choiceMessage.textContent = `Tu as choisi : ${playerChoice}`;
    resultContainer.textContent = `L'ordinateur a choisi: ${computerChoice}`;
  }
  

  function endGame() {
    let message = "";
    if (playerScore > computerScore) {
      message = "Bravo ! Tu as gagné !";
    } else if (playerScore < computerScore) {
      message = "L'ordinateur gagne !";
    } else {
      message = "égalité";
    }
    gameEndMessage.textContent = message;
    gameEndContainer.style.display = "block";
    gameEnded = true;
  }

  maxPointsInput.addEventListener("input", function () {
    maxPoints = parseInt(maxPointsInput.value);
  });
});

