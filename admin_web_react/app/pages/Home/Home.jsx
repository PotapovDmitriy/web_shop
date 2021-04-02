import React, { Component } from 'react'

import Load from '../../components/Load/Load.jsx'
import styles from './style.css'

export default class Home extends Component {
    constructor(params) {
        super(params);

        this.state ={
            user : undefined
        }
    }
    componentDidMount(){
        //TODO: Добавить получение информации о админе
        console.log('Component:Home TODO:Добавить получение данных о админе с сервера')
        let timeout = setTimeout((e)=>{
            this.setState({
                user : {
                    first_name : 'James',
                    second_name : 'Smith',
                    third_name : 'Jr.',
                    login : 'admin'
                }
            });
            clearTimeout(timeout);
        }, 1000);
    }

    render() {
        let user = this.state.user;
        return (
            <div className={styles.home}>
                {(user)
                ?<div className={styles.accauntBlock}>
                    <p><b>Name:</b> {user.second_name + ' ' + user.first_name + ' ' + user.third_name}</p>
                    <p><b>Login:</b> {user.login}</p>
                </div>
                :<Load color='#735a6a' size ='lg'></Load>}
            </div>
        )
    }
}
