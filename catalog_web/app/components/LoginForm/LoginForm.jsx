import React, { Component } from 'react'
import axios from 'axios'
import styles from './style.css'
import { API_HOST } from '../../app.jsx';

export default class LoginForm extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            username : '',
            password : ''
        };

        this.login = this.login.bind(this);
    }
    
    login(){
        axios.post(API_HOST+'/auth', {
            username : this.state.username,
            password : this.state.password
        }, {withCredentials : true})
        .then((res)=>{
            if(res.data.access_token){
                localStorage.setItem('jwt', res.data.access_token);
                this.props.close();
            }
            else{
                this.setState({
                    username : '',
                    password : ''
                });
            }
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    render() {
        return (
            <div className={styles.loginWindow}>
                <div className={styles.loginForm}>
                    <label>Username</label>
                    <input type='text' placeholder='Username' onChange={(e)=>{this.setState({username : e.target.value})}}/>
                    <label>Password</label>
                    <input type='password' placeholder='Password' onChange={(e)=>{this.setState({password : e.target.value})}}/>
                    <button onClick={this.login}>Login</button>
                    <button onClick={this.props.close}>Cancel</button>
                </div>
            </div>
        )
    }
}
