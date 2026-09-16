import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      const formData = new URLSearchParams();
      formData.append('username', email); // OAuth2 expects 'username'
      formData.append('password', password);

      const response = await fetch('http://localhost:8000/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData,
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.detail || 'Login failed');
      }
      
      // Store token and redirect
      localStorage.setItem('access_token', data.access_token);
      window.location.href = '/'; // Or use navigate('/')
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-zinc-900 rounded-2xl shadow-2xl overflow-hidden border border-zinc-800">
        <div className="p-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-white mb-2">Welcome Back</h2>
            <p className="text-zinc-400">Log in to Spotify Clone to continue.</p>
          </div>

          {error && (
            <div className="mb-6 p-4 bg-red-500/10 border border-red-500/50 rounded-xl">
              <p className="text-red-500 text-sm text-center font-medium">{error}</p>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2" htmlFor="email">
                Email address
              </label>
              <input
                id="email"
                type="email"
                required
                className="w-full px-4 py-3 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                placeholder="name@domain.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2" htmlFor="password">
                Password
              </label>
              <input
                id="password"
                type="password"
                required
                className="w-full px-4 py-3 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className={`w-full bg-green-500 hover:bg-green-400 text-black font-bold py-3 px-4 rounded-full transition-all duration-300 transform ${loading ? 'opacity-70 cursor-not-allowed' : 'hover:scale-[1.02] active:scale-[0.98]'}`}
            >
              {loading ? 'Logging in...' : 'Log In'}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-zinc-400">
              Don't have an account?{' '}
              <Link to="/signup" className="text-white hover:text-green-500 font-semibold transition-colors duration-200">
                Sign up
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
