import React, { Component } from 'react';
import axios from 'axios';

import Input from '../../components/Input/Input.jsx';
import Load from '../../components/Load/Load.jsx';
import styles from './style.css';
import Button from '../../components/Button/Button.jsx';

export default class AddCategory extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            categories : undefined,
            choosenCategory : undefined,
            categoriesClass : styles.hidden,
            errorClass : undefined,
            categoryName : ''
        };

        this.nillRef = React.createRef();

        this.createCategory = this.createCategory.bind(this);
    }

    componentDidMount(){
        axios.get('http://localhost:8010/categories')
        .then((res)=>{
            this.setState({
                categories : res.data.categories.filter((category)=>{
                    return !category.isNil;
                })
            });
        })
        .catch((er)=>{
            console.log(er);
            this.setState({
                categories: [{category_id : 1, name : 'first'},{category_id : 2, name : 'second'}]
            })
        })
    }
    
    createCategory(){
        if(this.state.categoryName === ''){
            this.setState({
                errorClass : styles.error
            });
            let timeout = setTimeout(()=>{
                this.setState({
                    errorClass : undefined
                });
                clearTimeout(timeout);
            }, 2000);
        } else{
            let data = {
                name : this.state.categoryName,
                parent_id : (this.state.choosenCategory)?this.state.choosenCategory.category_id:null,
                isNil : this.nillRef.current.checked
            };
            console.log(data);
            axios.post('http://localhost:8010/categories', data)
            .then((res)=>{
                const { history } = this.props;
                history.push('/all_categories');
                console.log(res);
            })
            .catch((er)=>{
                console.log(er);
            })
        }
    }

    render() {
        return (
            <div>
                {(this.state.categories)
                ?<div className={styles.addCategory}>
                    <h2 className={styles.h2}>Add category</h2>
                    <Input placeholder='Input category name' 
                        label='Category name' 
                        id='#category_name' 
                        onChange={(e)=>{this.setState({ categoryName : e.target.value})}}
                        className={this.state.errorClass}/>
                    <div className={styles.categoryBlock}>
                        <p className={styles.categoryDescription}>Parent category</p>
                        {(this.state.choosenCategory)
                        ?<p className={styles.choosenCategory} 
                            onClick={()=>{
                                this.setState({
                                    categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                })}}>{this.state.choosenCategory.name}</p>
                        :<p className={styles.choosenCategory} 
                            style={{color: '#cd851e'}} 
                            onClick={()=>{
                                this.setState({
                                    categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                    })}}>Choose parent category</p>}
                        <div className={this.state.categoriesClass}>
                            {this.state.categories.map((category)=>{
                                return <p key={category.category_id} 
                                    className={styles.category}
                                    onClick={()=>{
                                        this.setState({
                                            choosenCategory : category,
                                            categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                        })}}>{category.name}</p>})}
                        </div>
                    </div>
                    <div className={styles.nillBlock}>
                        <p className={styles.nillDiscription}>Final category: </p>
                        <input type='checkbox' className={styles.checkBox} ref={this.nillRef}/>
                    </div>
                    <Button value='Create' onClick={this.createCategory}></Button>
                </div>
                :<Load/>}
            </div>
        )
    }
}
