import '../Game/Game.css';

function Game() {
    const CARD_COVER = "https://opengameart.org/sites/default/files/card%20back%20blue.png";

    return (
        <div id="game-main">
            <div id="top">
                <div className="player" id="top-left">
                    <h1>Player 1</h1>
                    <h2>Stack: </h2>
                    <img className="card" src={CARD_COVER} alt=""></img>
                </div>
                <div className="player" id="top-right">
                    <h1>Player 2</h1>
                    <h2>Stack: </h2>
                    <img className="card" src={CARD_COVER} alt=""></img>
                </div>
            </div>
            <div id="bottom">
                <div id="bottom-left">
                    <div id="war-stack"></div>
                </div>
                <div id="bottom-right">
                    <button>CONTINUE</button>
                </div>
            </div>
        </div>
    );
}

export default Game;