/**
 * Utility functions for data processing
 */

export function formatData(data: any[]): any[] {
  if (!data || !Array.isArray(data)) {
    console.warn('Invalid data provided');
    return [];
  }
  
  return data.map(item => ({
    ...item,
    processed: true,
    timestamp: new Date().toISOString()
  }));
}

export function validateInput(input: string): boolean {
  return input && input.trim().length > 0;
}
