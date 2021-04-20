import React, { Component } from 'react'
import axios from 'axios'
import styles from './style.css'
import Input from '../../components/Input/Input.jsx'
import Button from '../../components/Button/Button.jsx'
import {API_GETEWAY_HOST} from './../../app.jsx';

export default class Login extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            username : '',
            password : ''
        };

        this.login = this.login.bind(this);
    }
    
    login(){
        axios.post(API_GETEWAY_HOST+'auth',{
            username : this.state.username,
            password : this.state.password
        },{withCredentials:true})
        .then((res)=>{
            if(res.data.access_token){
                localStorage.setItem('jwt', res.data.access_token);
                window.location.href = '/';
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
            <div className={styles.loginPage}>
                <div className={styles.login}>
                    <h2>Login</h2>
                    <div className={styles.inputsBlock}>
                        <Input id='username' label='Username'
                        placeholder='Input your username'
                        type='text'
                        value={this.state.username}
                        onChange={(e)=>{
                            this.setState({username : e.target.value
                        })}}></Input>
                        <Input id='password' label='Password'
                        placeholder='Input your password'
                        type='password'
                        value={this.state.password}
                        onChange={(e)=>{
                            this.setState({password : e.target.value
                        })}}></Input>
                    </div>
                    <Button onClick={this.login} value='Login' bgColor='#d58520'></Button>
                </div>
            </div>
        )
    }
}
