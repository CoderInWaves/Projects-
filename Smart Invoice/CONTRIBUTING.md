# Contributing to Smart Invoice Analytics

Thank you for your interest in contributing to Smart Invoice Analytics! This document provides guidelines and information for contributors.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature/fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## 📋 Development Setup

1. **Environment Setup**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Database Setup**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

3. **Run Development Server**
```bash
uvicorn main:app --reload
```

## 🎯 How to Contribute

### Bug Reports
- Use the GitHub issue tracker
- Include steps to reproduce
- Provide system information
- Include error messages/logs

### Feature Requests
- Describe the feature clearly
- Explain the use case
- Consider backward compatibility

### Code Contributions
- Follow existing code style
- Add tests for new features
- Update documentation
- Keep commits focused and atomic

## 📝 Code Style

- Use Python PEP 8 style guide
- Use meaningful variable names
- Add docstrings for functions
- Keep functions small and focused
- Use type hints where appropriate

## 🧪 Testing

- Test your changes locally
- Ensure all existing functionality works
- Add tests for new features
- Test with different data formats

## 📚 Documentation

- Update README.md if needed
- Add docstrings to new functions
- Update API documentation
- Include examples for new features

## 🔍 Pull Request Process

1. Update documentation
2. Add tests if applicable
3. Ensure CI passes
4. Request review from maintainers
5. Address feedback promptly

## 📞 Questions?

Feel free to open an issue for questions or join our discussions!