import '../Game/Game.css';
import { useDispatch } from 'react-redux';
import { drawTwoCards, getOneGameInfo, continueOneGame } from '../../store/game';

function Game({ game }) {
    const dispatch = useDispatch();
    const CARD_COVER = "https://opengameart.org/sites/default/files/card%20back%20blue.png";

    async function play() {
        if (game.played_1 && game.played_2) {
            await dispatch(continueOneGame(game.played_1.id, game.played_2.id)).then(() => dispatch(getOneGameInfo()));
        } else {
            const card_1 = game.player_1.stack[game.player_1.stack.length - 1].id;
            const card_2 = game.player_2.stack[game.player_2.stack.length - 1].id;
            await dispatch(drawTwoCards(card_1, card_2)).then(() => dispatch(getOneGameInfo()));
        }
    }

    return (
        <div id="game-main">
            <div id="top">
                <div className="player" id="top-left">
                    <h1>Player 1</h1>
                    <h2>Stack: {game.player_1.stack.length}</h2>
                    <img className="card" src={game.played_1 ? game.played_1.image : CARD_COVER} alt=""></img>
                    { game.played_1?.value > game.played_2?.value ? <p>Player 1 wins</p> : null }
                </div>
                <div className="player" id="top-right">
                    <h1>Player 2</h1>
                    <h2>Stack: {game.player_2.stack.length}</h2>
                    <img className="card" src={game.played_2 ? game.played_2.image : CARD_COVER} alt=""></img>
                    {game.played_1?.value < game.played_2?.value ? <p>Player 2 wins</p> : null}
                </div>
            </div>
            <div id="bottom">
                <div id="bottom-left">
                    <div id="war-stack">
                        {game.war.length}
                    </div>
                </div>
                <div id="bottom-right">
                    <button onClick={play}>CONTINUE</button>
                </div>
            </div>
        </div>
    );
}

export default Game;