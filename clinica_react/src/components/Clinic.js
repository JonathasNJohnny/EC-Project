import React, { Component } from 'react';
import './Clinic.css'

export default class Clinic extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            password: '',
        };
    }

    handleNameChange = (event) => {
        this.setState({ name: event.target.value});
    }

    handlePasswordChange = (event) => {
        this.setState({ password: event.target.value});
    }

    handleLogin = () => {
        // Você pode acessar os valores do estado name e password aqui
        console.log('Name:', this.state.name);
        console.log('Password:', this.state.password);
    }

    render() {
        return (
            <div className='clinic' id="myCode">
                <form>
                    <label id="labelInsert">Name: </label>
                    <input type="text" id="loginNameInsert" name="user_name" value={this.state.name} onChange={this.handleNameChange} /><br></br>
                    <label id="labelInsert">Password: </label>
                    <input type="text" id="loginPasswordInsert" name="user_name" value={this.state.password} onChange={this.handlePasswordChange} /><br></br>
                    <button type="button" id="loginButton" onClick={this.handleLogin}>Login</button>
                </form>
            </div>
        )
    }
}