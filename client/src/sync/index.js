/**
 * Syncs the React client and the server using an SSE listener and HTTP
 * POST requests.
 */
import {createStore} from "redux";

const RECEIVE_ROBOT_SPEED = "RECEIVE_ROBOT_SPEED";
const RECEIVE_CHALLENGE_LAUNCHED = "RECEIVE_CHALLENGE_LAUNCHED";
const RECEIVE_CHALLENGE_CANCELLED = "RECEIVE_CHALLENGE_CANCELLED";
