function showToast(title, message, type = 'info', duration = 3000) {
  const toast = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastDot = document.getElementById('toast-icon');
  if (!toast) return;

  // Base neutral style: gray background, angular, default blue border
  toast.classList.remove(
    'bg-red-50','text-red-600','bg-green-50','text-green-600','bg-white','border-gray-300','text-gray-800'
  );
  toast.classList.add('bg-gray-50','text-gray-800','rounded-md');

  // Determine colors per type
  const colors = {
    success: { border: '#22c55e', dot: '#22c55e' },
    error:   { border: '#ef4444', dot: '#ef4444' },
    info:    { border: '#3b82f6', dot: '#3b82f6' },
    normal:  { border: '#3b82f6', dot: '#3b82f6' },
  };
  const c = colors[type] || colors.info;
  toast.style.border = `1px solid ${c.border}`;
  if (toastDot) {
    toastDot.className = 'inline-block w-2.5 h-2.5 rounded-full flex-shrink-0';
    toastDot.style.background = c.dot;
  }

  toastTitle.textContent = title || '';
  toastMessage.textContent = message || '';

  try {
    const audio = new Audio('/static/sound/ding.mp3');
    audio.play().catch(() => {});
  } catch (e) {}

  toast.classList.remove('opacity-0', 'translate-y-64');
  toast.classList.add('opacity-100', 'translate-y-0');

  setTimeout(() => {
    toast.classList.remove('opacity-100', 'translate-y-0');
    toast.classList.add('opacity-0', 'translate-y-64');
  }, duration);
}
