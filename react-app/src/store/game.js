const initialState = {};

const GET_GAME_INFO = 'game/GAME_INFO';
const getGameInfo = gameInfo => ({
    type: GET_GAME_INFO,
    gameInfo
});
export const getOneGameInfo = () => async dispatch => {
    const response = await fetch('/api/game');
    const gameInfo = await response.json();
    dispatch(getGameInfo(gameInfo));
}

const START_GAME = 'game/START_GAME';
const startGame = () => ({
    type: START_GAME
});
export const startOneGame = () => async dispatch => {
    await fetch('/api/game/start', { method: 'PUT' });
    dispatch(startGame());
}

const DRAW_CARDS = 'game/DRAW_CARDS';
const drawCards = () => ({
    type: DRAW_CARDS
});
export const drawTwoCards = (card_1, card_2) => async dispatch => {
    await fetch('/api/game/draw', { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ card_1, card_2 }) });
    dispatch(drawCards());
}

const CONTINUE_GAME = 'game/CONTINUE_GAME';
const continueGame = () => ({
    type: CONTINUE_GAME
});
export const continueOneGame = (card_1, card_2) => async dispatch => {
    await fetch('/api/game/continue', { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ card_1, card_2 }) });
    dispatch(continueGame());
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_GAME_INFO:
            state = action.gameInfo;
            return state;
        case START_GAME:
            return state;
        case DRAW_CARDS:
            return state;
        case CONTINUE_GAME:
            return state;
        default:
            return state;
    }
}