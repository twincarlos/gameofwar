function Winner({ game }) {
    return (
        <div>
            { game.player_1.stack.length ? <h1>Player 1 Wins!</h1> : <h1>Player 2 Wins!</h1> }
            <button>Home</button>
        </div>
    );
}

export default Winner;