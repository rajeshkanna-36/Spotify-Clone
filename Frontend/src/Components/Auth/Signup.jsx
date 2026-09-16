import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Signup = () => {
  const [formData, setFormData] = useState({
    user_name: '',
    email_id: '',
    mobile_number: '',
    date_of_birth: '',
    password: ''
  });

  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      // Clean up empty optional fields
      const payload = { ...formData };
      if (!payload.date_of_birth) payload.date_of_birth = null;
      if (!payload.mobile_number) payload.mobile_number = null;

      const response = await fetch('http://localhost:8000/api/auth/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.detail || 'Signup failed');
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
            <h2 className="text-3xl font-bold text-white mb-2">Create Account</h2>
            <p className="text-zinc-400">Join Spotify Clone and start listening.</p>
          </div>

          {error && (
            <div className="mb-6 p-4 bg-red-500/10 border border-red-500/50 rounded-xl">
              <p className="text-red-500 text-sm text-center font-medium">{error}</p>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-1" htmlFor="user_name">
                Full Name
              </label>
              <input
                id="user_name"
                name="user_name"
                type="text"
                required
                className="w-full px-4 py-2.5 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                placeholder="John Doe"
                value={formData.user_name}
                onChange={handleChange}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-1" htmlFor="email_id">
                Email address
              </label>
              <input
                id="email_id"
                name="email_id"
                type="email"
                required
                className="w-full px-4 py-2.5 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                placeholder="name@domain.com"
                value={formData.email_id}
                onChange={handleChange}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-zinc-300 mb-1" htmlFor="mobile_number">
                  Mobile (Optional)
                </label>
                <input
                  id="mobile_number"
                  name="mobile_number"
                  type="tel"
                  className="w-full px-4 py-2.5 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                  placeholder="+1 234 567 890"
                  value={formData.mobile_number}
                  onChange={handleChange}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-zinc-300 mb-1" htmlFor="date_of_birth">
                  Date of Birth
                </label>
                <input
                  id="date_of_birth"
                  name="date_of_birth"
                  type="date"
                  className="w-full px-4 py-2.5 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300 [color-scheme:dark]"
                  value={formData.date_of_birth}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-1" htmlFor="password">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="w-full px-4 py-2.5 bg-zinc-800/50 border border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 text-white placeholder-zinc-500 transition-all duration-300"
                placeholder="••••••••"
                value={formData.password}
                onChange={handleChange}
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className={`w-full mt-2 bg-green-500 hover:bg-green-400 text-black font-bold py-3 px-4 rounded-full transition-all duration-300 transform ${loading ? 'opacity-70 cursor-not-allowed' : 'hover:scale-[1.02] active:scale-[0.98]'}`}
            >
              {loading ? 'Signing up...' : 'Sign Up'}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-zinc-400">
              Already have an account?{' '}
              <Link to="/login" className="text-white hover:text-green-500 font-semibold transition-colors duration-200">
                Log in
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;
