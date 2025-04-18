import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../utils/authentication/AuthProvider";

import AuthForm from "../../components/LoginForm/LoginForm";
import Layout from "../../components/Layout/Layout";



const Login = ({ initialMethod }) => {
    const [method, setMethod] = useState(initialMethod);

    const { isAuthorized } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthorized) {
            navigate("/account/profile");
        }
    }, [isAuthorized, navigate])





    useEffect(() => {
        setMethod(initialMethod);
    }, [initialMethod]);

    const route = method === 'login' ?  '/authentication/dj-rest-auth/login/': '/authentication/dj-rest-auth/registration/';

    return (
        <Layout>
            <div>
                <AuthForm route={route} method={method} />
            </div>
        </Layout>
    )
}
export default Login;