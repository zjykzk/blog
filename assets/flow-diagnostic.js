(() => {
  const form = document.querySelector('[data-flow-form]');
  if (!form) return;

  const result = document.querySelector('[data-flow-result]');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const elapsed = Number(data.get('elapsed'));
    const active = Number(data.get('active'));
    const handoffs = Number(data.get('handoffs'));
    const longestWait = String(data.get('longestWait') || '').trim();

    if (!elapsed || active < 0 || active > elapsed || handoffs < 0) {
      result.dataset.visible = 'true';
      result.innerHTML = '<strong>请检查数据：</strong>总历时必须大于 0，工作时间不能超过总历时，交接次数不能为负。';
      return;
    }

    const wait = elapsed - active;
    const efficiency = Math.round((active / elapsed) * 100);
    let diagnosis = '先检查最长等待点；那里通常比“让每个人更快”更有杠杆。';
    if (handoffs >= 4) diagnosis = '交接较多。先确认每次交接是否真的需要不同角色或团队。';
    if (efficiency >= 70 && handoffs < 4) diagnosis = '这件工作的流动尚可；不要仅凭单一样本下结论，再抽取两件不同类型的工作。';

    result.dataset.visible = 'true';
    result.innerHTML = `<strong>流动画像：</strong>${elapsed} 天里约 ${wait} 天在等待，活跃工作占 ${efficiency}%，经历 ${handoffs} 次交接。<br><strong>第一假设：</strong>${diagnosis}${longestWait ? `<br><strong>你记录的最长等待：</strong>${escapeHtml(longestWait)}` : ''}`;
  });

  function escapeHtml(value) {
    const node = document.createElement('span');
    node.textContent = value;
    return node.innerHTML;
  }
})();
