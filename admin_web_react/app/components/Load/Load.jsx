import React, { Component } from 'react'
import styles from './style.css'

export default class Load extends Component {
    render() {
        return (
            <div className={styles.load}>
                <box-icon name='loader-circle' color={this.props.color} animation='spin' size={this.props.size}></box-icon>
            </div>
        )
    }
}
