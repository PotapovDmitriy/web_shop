import React, { Component } from 'react'

import styles from './style.css'

export default class Button extends Component {
    render() {
        return (
            <button className={styles.button} onClick={this.props.onClick}>{this.props.value.toUpperCase()}</button>
        )
    }
}
