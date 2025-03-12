import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Nav from "./components/Nav/Nav";

import { AuthProvider } from "./utils/authentication/AuthProvider"; // global authentication context

// Pages
import Index from "./pages/Index/Index";
import About from "./pages/About/About";
import Contact from "./pages/Contact/Contact";
import Faq from "./pages/Faq/Faq";
import Shop from "./pages/Shop/Shop";
import Login from "./pages/Login/Login";
import Profile from "./pages/Profile/Profile";

import PasswordReset from "./pages/PasswordReset/PasswordReset";
import PasswordConfirm from "./pages/PasswordConfirm/PasswordConfirm";

import VerifyEmail from "./pages/VerifyEmail/VerifyEmail";
import EmailConfirm from "./pages/EmailConfirm/EmailConfirm";

function App() {

    return (
        <AuthProvider>
            <Router>
                <Nav />
                <Routes>

                    {/* common route */}
                    <Route path="/" element={<Index />} />
                    <Route path="/about" element={<About />} />
                    <Route path="/shop" element={<Shop />} />
                    <Route path="/faq" element={<Faq />} />
                    <Route path="/contact" element={<Contact />} />
                    <Route path="/profile" element={<Profile />} />

                    {/* general auth routes */}
                    <Route path="/account/login" element={<Login initialMethod="login" />} />
                    <Route path="/account/register" element={<Login initialMethod="register" />} />
                    <Route path="/account/password/recover" element={<PasswordReset />} />

                    {/* redirect from email auth routes */}
                    <Route path="/account/verify-email/:email" element={<VerifyEmail/>} />
                    <Route path="/account/password-reset/confirm/:uid/:token" element={<PasswordConfirm/>} />
                    <Route path="/account/confirm-email/:uid/:token" element={<EmailConfirm />} />



                    {/* if route dne */}
                    <Route path="/*" element={<Navigate to="/" />} />
                </Routes>
            </Router>

        </AuthProvider>
    )
}

export default App;
