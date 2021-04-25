import React, { Component } from 'react'
import classnames from 'classnames'

import styles from './style.css'

export default class Input extends Component {
    render() {
        return (
            <div className={styles.inputBlock}>
                <label htmlFor={this.props.id} className={classnames(styles.label, this.props.className)}>{this.props.label}</label>
                <input id={this.props.id} 
                    placeholder={this.props.placeholder}
                    className={classnames(styles.input, this.props.className)}
                    onChange={(e)=>{this.props.onChange(e)}}
                    value={this.props.value}
                    type={(this.props.type)?this.props.type:'text'}></input>
            </div>
        )
    }
}
