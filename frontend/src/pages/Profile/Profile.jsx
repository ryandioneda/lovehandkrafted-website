import { useEffect } from "react";
import { useAuth } from "../../utils/authentication/AuthProvider";
import { useNavigate } from "react-router-dom";
import Layout from "../../components/Layout/Layout";

const Profile = () => {
    console.log("Profile");

    const { isAuthorized, handleLogout } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (!isAuthorized) {
            navigate("/account/login");
        }
    }, [isAuthorized, navigate]);


    return (
        <Layout>
            <div id="index-root" className="h-screen bg-red-500 flex justify-center items-center">
                <button 
                    onClick={handleLogout} // 
                    className="px-4 py-2 bg-white text-black rounded-md shadow-md hover:bg-gray-300 transition"
                >
                    Logout
                </button>
            </div>
        </Layout>
    )

}

export default Profile;